from rest_framework import serializers
from .forms import SignupForm

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignupForm
        fields = ('email', 'first_name', 'last_name')