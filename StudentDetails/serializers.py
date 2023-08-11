from rest_framework import serializers
from .models import StudentDetails, StudentMarks

class StudentMarksSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentMarks
        fields = ['admission', 'SUB1', 'SUB2', 'SUB3']

        extra_kwargs = {

            'SUB1' : {'max_value' : 100, 'min_value' : 0},
            'SUB2' : {'max_value' : 100, 'min_value' : 0},
            'SUB3' : {'max_value' : 100, 'min_value' : 0},
        }

class StudentDetailsSerializer(serializers.ModelSerializer):

    marks = StudentMarksSerializer(read_only = True)

    def validate(self, attrs):
        ph = attrs['phone']
        nm = attrs['name']
        id = attrs['id']

        if (len(str(ph)) != 10):
            raise serializers.ValidationError('Enter correct number')
        
        if (nm.replace(' ', '').isalpha()== False):
            raise serializers.ValidationError('Enter correct name')
        
        if (len(str(id))) == 1:
            attrs['student_id'] = 'STD_0' + str(id)
        if (len(str(id))) > 1:
            attrs['student_id'] = 'STD_' + str(id)  
        return attrs
    

    class Meta:
        model = StudentDetails
        fields = ['id', 'student_id', 'branch', 'name', 'phone', 'email', 'address', 'photo', 'marks']
        read_only_fields = ['marks', 'student_id']

        extra_kwargs = {
            'id' : {'min_value' : 1},
        }
