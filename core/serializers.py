from rest_framework import serializers
from core.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Transaction
        fields = ("id", "code")