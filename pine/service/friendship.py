from pine.models import Users, Phones


def create_friendship(user, target_phone_number):
    # get or create target phone record
    target_phone_id = Phones.objects.filter(phone_number=target_phone_number)
    target_phone = None
    if target_phone_id.exists():
        target_phone = target_phone_id[0]
    else:
        target_phone = Phones.objects.create(phone_number=target_phone_number)

    # check for performance.
    # If does not need to compute it return
    if user.friend_phones.filter(phone_number=target_phone_number).exists():
        return

    # add target phone to friends phones
    user.friend_phones.add(target_phone)

    # check for performance.
    # If target is no pine user it return
    target_user_query = Users.objects.filter(phone=target_phone)
    target_user = None
    if target_user_query.exists():
        target_user = target_user_query[0]
    else:
        return

    # configure friends, following
    has_user_target_phone = target_user.friend_phones.filter(id=user.id).exists()
    if has_user_target_phone:
        user.friends.add(target_user)
    else:
        user.followings.add(target_user)