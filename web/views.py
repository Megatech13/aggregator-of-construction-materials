from datetime import datetime
from django.shortcuts import render, redirect
# from mysite.web.models import Requests



# reqmat_data - requests material - заявки на материал (унести в базу данных)
reqmat_db = [
    {
        'id': 0,
        'author': "Игорешка",
        'delivery_date': datetime.now(),
        'address': 'Путину на дачу',
        'description': 'Везите весь каширский двор нахуй, тут сами выберем',
        'offers': [
            {
                'id': 0,
                'name_of_provider': 'Мега',
                'date': '28.09.2020',
                'price': '28000 руб'
            },
            {
                'id': 1,
                'name_of_provider': 'Игорь',
                'date': '27.09.2020',
                'price': '2 000 руб'
            },
            {
                'id': 2,
                'name_of_provider': 'Манас',
                'date': 'завтра',
                'price': 'бесплатно'
            }

        ]

    },
    {
        'id': 1,
        'author': "Мергешка",
        'delivery_date': datetime.now(),
        'address': '1-й котляковский переулок д1А стр1',
        'description': 'Нужен материал для штукатурных работ и стяжки пола'
                       '1м ротбанд'
                       'каменный цветок ЦПС дохера надо на 1000м2',
        'offers': []

    },
    {
        'id': 2,
        'author': "Иполит",
        'delivery_date': datetime.now(),
        'address': 'хуй занет куда',
        'description': 'Нужен материал для ремонта под ключ мозга жены',
        'offers': []

    }
]
# adminmessages - сообщения администратору (унести в базу данных)
adminmessages_db = [
    {
        'id': 0,
        'name': 'Мега',
        'email': 'imeg@list.ru',
        'text': 'Почините балять уже, что-нибудь'
    },
    {
        'id': 1,
        'name': 'Олех',
        'email': 'oleh@mail.com',
        'text': 'Крутой сервис ептить'
    },
    {
        'id': 2,
        'name': 'Angelica',
        'email': 'iwantyou@mail.com',
        'text': 'cyberpunk рулит'
    }
]


def index(request):
    return render(request, 'index.html')


def contacts(request):
    if request.method == 'GET':
        return render(request, 'contacts.html')
    else:
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']

        if len(name) == 0 or len(email) == 0 or len(text) == 0:
            return render(request, 'contacts.html', {'error': 'Не заполнены поля'})

        adminmessages_db.append({
            'id': len(adminmessages_db),
            'name': name,
            'email': email,
            'text': text
        })

        return render(request, 'contacts.html', {'success': 'Спасибо, ваше сообщение отправлено'})


def wantlist(request):
    return render(request, 'wantlist.html', {
        'wantlist': reqmat_db
    })


def wantlist_item(request, id):
    if request.method == 'GET':
        if id <= len(reqmat_db):
            return render(request, 'wantlist_item.html', reqmat_db[id])
        else:
            return redirect('/wantlist')
    else:
        name_of_provider = request.POST['name_of_provider']
        date = request.POST['date']
        price = request.POST['price']

        if len(name_of_provider) == 0 or len(date) == 0 or len(price) == 0:
            return render(request, 'wantlist_item.html', reqmat_db[id])

        reqmat_db[id]['offers'].append({
            'id': len(reqmat_db[id]['offers']),
            'name_of_provider': name_of_provider,
            'date': date,
            'price': price
        })

        return render(request, 'wantlist_item.html', reqmat_db[id])


def newrequest(request):
    if request.method == 'GET':
        return render(request, 'newrequest.html')
    else:
        delivery_date = request.POST['delivery_date']
        address = request.POST['address']
        description = request.POST['description']
        author = request.POST['author']

        if len(delivery_date) == 0 or len(address) == 0 or len(description) == 0 or len(author) == 0:
            return render(request, 'newrequest.html', {'error': 'Не заполненны поля'})

        reqmat_db.append({
            'id': len(reqmat_db),
            'author': author,
            'delivery_date': delivery_date,
            'address': address,
            'description': description
        })
        # Requests(delivery_date=delivery_date, address=address, description=description, author=author)
        return redirect('/wantlist')


def adminmessages(request):
    return render(request, 'adminmessages.html', {
        'adminmessages': adminmessages_db
    })


def adminmessage(request, number):
    if number <= len(adminmessages_db):
        return render(request, 'adminmessage.html', adminmessages_db[number])
    else:
        return redirect('/')
