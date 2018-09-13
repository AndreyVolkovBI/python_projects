# Vk API Keys
firstKey = 'bdd4f04384e64fca69b320980a74f961b1a6913d4af63bb03beb114f1d64bf962f44dc60669f3da551d3d'
secondKey = 'f700d6a156da79e4098f43129f324600622dcede098a23a82eb3438ea994161aff9a0a3fc49a345255a04'
thirdKey = '9b2df091db5e56d63d1f73733c07dbf8f1334e1cb7d3898e70271d84dd6278e57d83d5c9476b6baa3561e'
fourthKey = '0e6849e454334d8f3ce3c0215448d33db31e45b752c4442633338c95a040d89fd5d5376c17f1285a29c1c'

firstPair = {1: firstKey, 2: secondKey}
secondPair = {1: thirdKey, 2: fourthKey}

# Vk API Constants
api_url = 'https://api.vk.com/method/'
method_name_friends = 'friends.get?'
method_name_user = 'users.get?'
method_name_execute = 'execute?'
access_token = 'access_token='
vk_token = '1413b3ae02dd070b7d7b62d11c75ccc47a47f108f60622eeb3225396b50a167796fda501b07bb8c6c516d'
version = 'v=5.84'

# users.get
usersGet = api_url + method_name_user + 'user_ids=' + '{0}' + '&fields=photo_100' + '&' + access_token + firstPair[1] + '&' + version

# friends.get
friendsGet = api_url + method_name_friends + 'user_id=' + '{0}' + '&' + access_token + firstPair[1] + '&' + version

# execute
executeGet = api_url + method_name_execute + 'code={}&' + access_token + '{}' + '&' + version

# errors
noSuchUser = {'error': {'code': '001', 'message': 'The user is not found'}}
noFriends = {'error': {'code': '002', 'message': 'The user either does not have or has hidden friends'}}
tooFar = {'error': {'code': '002', 'message': 'The distance between two users is too far'}}