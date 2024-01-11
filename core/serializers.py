from rest_framework import serializers
from core.models import Bill, Plate

class PlateSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Plate
        fields = ['bill', 'order', 'name', 'price']

class BillSerializer(serializers.ModelSerializer):
    plates = PlateSerializer(many=True)

    class Meta:
        model = Bill
        fields = ['name', 'table_code', 'plates']

    def create(self, validated_data):
        plates_data = validated_data.pop('plates')
        bill = Bill.objects.create(**validated_data)
        for plate_data in plates_data:
            Plate.objects.create(bill=bill, **plates_data)
        return bill