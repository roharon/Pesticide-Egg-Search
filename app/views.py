from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .db_to import db_to_views
from .loading import loading_list
import json



def keyboard(request):

    return JsonResponse({
            'type': 'buttons',
            'buttons': ['달걀 검사하기']
    })

@csrf_exempt
def message(request):
    json_str = (request.body).decode('utf-8')
    received_json_data = json.loads(json_str)
    content_name = received_json_data['content']
    content_type = received_json_data['type']

    content_name = str(content_name).upper()

    if content_name == '달걀 검사하기':
        return JsonResponse({
            'text': {
                'type': 'text'
            },
            'message': {
                'text': '달걀에 쓰여진 문자를 입력해주세요!(꺄아)'
            }
        })

    egg_list = db_to_views()
    all_list = []
    #print((egg_list))

    for i in range(0, len(egg_list)):
        all_list.append(egg_list[i][0])
    print(all_list)
    if content_name in all_list:
        answer = '살충제 달걀 상품입니다.'
    else:
        answer = '안전한 달걀 상품입니다.'


    if content_type == 'photo':
        answer = '사진기능은 지원하지 않아요'
    elif content_type == 'video':
        answer = '영상기능은 지원하지 않아요'
    elif content_type == 'audio':
        answer = '녹음파일은 지원하지 않아요'
    else:
        pass

    return JsonResponse({
        'message': {
            'text': answer
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': ['달걀 검사하기']
        }

    })




