import uuid
from telegram import Update
from telegram.ext import ContextTypes


from db.models import UserProfile
from db.changers import add_object
from apps.converters import compose_profile_from


def add_user_id_to_context(update: Update, context: ContextTypes.DEFAULT_TYPE) -> uuid.UUID:
    assert update.message and update.message.from_user and context.user_data is not None

    if context.user_data.get('user_id'):
        user_id_in_context: uuid.UUID = context.user_data['user_id']
        return user_id_in_context

    user_id_in_db = UserProfile.find_profile_id_by_telegram_id(update.message.from_user.id)
    if user_id_in_db:
        context.user_data['user_id'] = user_id_in_db
        return user_id_in_db

    new_profile = compose_profile_from(
        update.message.from_user.id,
        update.message.from_user.full_name,
    )
    add_object(new_profile)
    context.user_data['user_id'] = new_profile.user_id
    return new_profile.user_id
