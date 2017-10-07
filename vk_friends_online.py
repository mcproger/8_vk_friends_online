import vk
import getpass
import argparse


def get_console_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('vk_app_id', type=str)
    args = parser.parse_args()
    return args


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
        scope='friends',
    )
    api = vk.API(session)
    return api


def format_output_online_friend(online_friend_info):
    online_friend = '{first_name} {last_name}'.format(
        first_name=online_friend_info['first_name'],
        last_name=online_friend_info['last_name'],
    )
    return online_friend


if __name__ == '__main__':
    args = get_console_arguments()
    app_id = args.vk_app_id
    login = get_user_login()
    password = get_user_password()
    vk_api = get_vk_api_session(app_id, login, password)
    online_friends_id_list = vk_api.friends.getOnline()
    online_friends_info = vk_api.users.get(user_ids=online_friends_id_list)
    for online_friend_info in online_friends_info:
        print(format_output_online_friend(online_friend_info))
