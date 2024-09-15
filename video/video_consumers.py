
import json
import os
from django.core.files.base import ContentFile
from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings
from video.models.video import Video
from video.models.category import Category


class VideoUploadConsumer(AsyncWebsocketConsumer):
    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            data = json.loads(text_data)
            category_id = data.get('category_id')
            category = Category.objects.get(id=category_id)

        if bytes_data:
            file_data = bytes_data
            file_name = f"uploaded_video_{self.scope['user'].id}.mp4"
            file_path = os.path.join(settings.MEDIA_ROOT, 'videos', file_name)

            with open(file_path, 'wb') as f:
                f.write(file_data)

            file_size = os.path.getsize(file_path)

            Video.objects.create(
                file=file_name,
                size=file_size,
                category=category,
            )

            await self.send(text_data=json.dumps({
                'status': 'success',
                'file_info': {
                    'file_name': file_name,
                    'file_size': file_size,
                }
            }))
