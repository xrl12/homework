from rest_framework_jwt.serializers import serializers

from .models import JokeDuanzi, JokeImg


class JokeDuanziSerializer(serializers.ModelSerializer):
    nvum = serializers.IntegerField()
    like_num = serializers.IntegerField()

    class Meta:
        fields = '__all__'
        model = JokeDuanzi

    def validate_nvum(self, nvum):
        if nvum != 0:
            raise serializers.ValidationError('别想作弊偶')
        return nvum

    def validate_like_num(self, like_num):
        if like_num != 0:
            raise serializers.ValidationError('别想作弊偶')
        return like_num

    def validate_no_like(sel,no_like):
        if no_like != 0:
            raise serializers.ValidationError('别想作弊偶')
        return no_like

    def validate_is_hot(self, is_hot):
        if is_hot == 1 or is_hot == 0:
            return is_hot
        raise serializers.ValidationError('支支持一和0,1表示热点新闻,2表示不是热点新闻')


class JokeImgSerializer(serializers.ModelSerializer):
    nvum = serializers.IntegerField()
    like_num = serializers.IntegerField()
    no_like = serializers.IntegerField()

    class Meta:
        fields = "__all__"
        model = JokeImg

    def validate_nvum(self, nvum):
        if nvum != 0:
            raise serializers.ValidationError('不可以开挂偶')
        return nvum

    def validate_no_like(self, no_like):
        print(no_like)
        if no_like != 0:
            raise serializers.ValidationError('不可以开挂偶')
        return no_like

    def validate_like_num(self, like_num):
        if like_num != 0:
            raise serializers.ValidationError('不可以开挂偶')
        return like_num
