from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SentimentRequestSerializer, SentimentResponseSerializer
from textblob import TextBlob
# import textblob
# textblob.download_corpora.download_all()

class SentimentAnalysisView(APIView):
    def post(self, request):
        serializer = SentimentRequestSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity

            if polarity > 0.1:
                sentiment = "positive"
            elif polarity < -0.1:
                sentiment = "negative"
            else:
                sentiment = "neutral"

            response = SentimentResponseSerializer({"sentiment": sentiment})
            return Response(response.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
