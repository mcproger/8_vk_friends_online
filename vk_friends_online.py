import vk
import getpass
import time


def get_user_login():
    user_login = input('Enter login from vk.com: ')
    return user_login


def get_user_password():
    user_password = getpass.getpass('Enter password from vk.com: ')
    return user_password


def get_vk_api_session(app_id, login, password):
    session = vk.AuthSession(
        app_id=app_id,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    return api


def get_online_friends_id_list(vk_api):
    online_friends_id_list = vk_api.friends.getOnline()
    return online_friends_id_list


def output_friends_to_console(vk_api, online_friend_id):
    online_friend_info = vk_api.users.get(user_ids=online_friend_id)
    too_many_requests_time_delay = 0.5
    time.sleep(too_many_requests_time_delay)
    online_friend = '{first_name} {last_name}'.format(
        first_name=online_friend_info[0]['first_name'],
        last_name=online_friend_info[0]['last_name']
    )
    return online_friend


if __name__ == '__main__':
    app_id = -1  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev
    login = get_user_login()
    password = get_user_password()
    vk_api = get_vk_api_session(app_id, login, password)
    online_friends_id_list = get_online_friends_id_list(vk_api)
    for online_friend_id in online_friends_id_list:
        print(output_friends_to_console(vk_api, online_friend_id))
