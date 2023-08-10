from rest_framework import serializers
from .models import StudentDetails


class StudentDetailsSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        ph = attrs['phone']
        nm = attrs['name']
        id = attrs['student_id']

        if (len(str(ph)) != 10):
            raise serializers.ValidationError('Enter correct number')
        
        if (nm.replace(' ', '').isalpha()== False):
            raise serializers.ValidationError('Enter correct name')
        
       # if (len(str(id))) == 1:
      #      attrs['student_id'] = 'STD_0' + str(id)
      #  if (len(str(id))) > 1:
       #     attrs['student_id'] = 'STD_' + str(id)  
        return attrs

    class Meta:
        model = StudentDetails
        fields = '__all__'
