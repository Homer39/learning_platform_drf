from rest_framework import serializers


class LinkValidator:
    """Валидатор проверяет корректность ссылки на видео"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        """Можно добавлять только сслыки на youtube"""
        if 'www.youtube' not in value:
            raise serializers.ValidationError('Допустимы ссылки только на youtube')
