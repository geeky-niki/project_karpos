from rest_framework import serializers
from ..models import daily_transection

# create a basic serializer clas
class karpos_serializer (serializers.Serializer):
  cust_id = serializers.IntegerField()
  cust_name =serializers.CharField()
  product_bought = serializers.CharField()
  product_price = serializers.DecimalField(max_digits=5, decimal_places=2)
  quantity = serializers.IntegerField()
  is_regular = serializers.BooleanField()


  #write create function
  def create(self, validated_data):
    return daily_transection.objects.create(**validated_data) 

  #write update functiom
  def update(self, instance, validated_data):
    instance.cust_id = validated_data.get('cust_id', instance.cust_id)
    instance.cust_name = validated_data.get('cust_name', instance.cust_name)
    instance.product_bought = validated_data.get('product_bought', instance.product_bought)
    instance.product_price = validated_data.get('product_price', instance.product_price)
    instance.quantity = validated_data.get('quantity', instance.quantity)
    instance.is_regular = validated_data.get('is_regular', instance.is_regular)
    return instance

  #filed level validation
  def validate_quantity(self, value):
    if value < 0 :
      raise serializers.ValidationError("quantity can not be negative")
    else:
      return value

  # object level validation
  def validate(self, data):
    # Check if any field value is empty
    for field, value in data.items():
        if value is None or value == '':
            raise serializers.ValidationError(f"The field '{field}' cannot be empty.")
    return data
