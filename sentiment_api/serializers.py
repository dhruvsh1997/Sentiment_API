from rest_framework import serializers

class SentimentRequestSerializer(serializers.Serializer):
    text = serializers.CharField()

class SentimentResponseSerializer(serializers.Serializer):
    sentiment = serializers.ChoiceField(choices=["positive", "neutral", "negative"])
