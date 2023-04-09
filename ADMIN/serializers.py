from rest_framework import serializers
from .models import AdminSetting

class AdminSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdminSetting
        fields=[ 
            'header_image',
            'payment_charge'
        ]



