import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import KeyWordsData, VideoData
from .serializers import KeyWordsSerializer, VideoDataSerializer
# Create your views here.


class KeyWordsAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def get(self, request):
        key_words = KeyWordsData.objects.all()
        serializer = KeyWordsSerializer(key_words, many=True)
        return Response(serializer.data)

    def post(self, request):
        key_word = request.data
        print(key_word)
        serializer = KeyWordsSerializer(data=key_word)
        if serializer.is_valid(raise_exception=False):
            key_world_saved = serializer.save()
            return Response({"success": "key world {} add successfully".format(key_world_saved.key_word)})
        else:
            return Response({"error": 'Error add key word'})

    def delete(self, request, pk):
        # Get object with this pk
        try:
            key_word = KeyWordsData.objects.get(pk=pk)
            key_word.delete()
            return Response({
                    "message": "Key world with id {} has been deleted.".format(pk)
                }, status=204)
        except KeyWordsData.DoesNotExist:
            return Response({
                "message": "Key world with id {} does not exist.".format(pk)
            }, status=404)


class VideoDataAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def get(self, request, pk):
        date_gte = request.GET.get('date__gte', None)
        date_lte = request.GET.get('date__lte', None)
        video_list = VideoData.objects.filter(key_word__id=pk)
        if date_gte:
            date_gte = datetime.datetime.strptime(date_gte, '%d.%m.%Y')
            video_list = video_list.exclude(published_at__lt=date_gte)
        if date_lte:
            date_lte = datetime.datetime.strptime(date_lte, '%d.%m.%Y')
            video_list = video_list.exclude(published_at__gt=date_lte)
        page = request.GET.get('page', None)
        try:
            if page and video_list.count() > 10:
                page = int(page)
                start_index = (page - 1) * 10
                start_index = start_index if 0 <= start_index < video_list.count() else 0
                end_index = start_index + 9
                end_index = end_index if end_index <= video_list.count() else video_list.count() - 1
                video_list = video_list[start_index:end_index]
        except ValueError:
            pass
        # video_list = video_list.order_by('-published_at')
        serializer = VideoDataSerializer(video_list, many=True)
        return Response(serializer.data)


