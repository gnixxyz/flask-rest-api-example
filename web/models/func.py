
from .base import db
from .user import User


def user_loader(identity):
    return User.query.get(identity)


def build_query(model_clss):
    return db.session.query(model_clss)


def fetch_ids_with_cursor(model_class, filter_func=None, **kwargs):
    cursor = kwargs.get('cursor', 0)
    limit = kwargs.get('limit', 10)
    order = kwargs.get('order', 'desc')
    is_desc = order != 'asc'

    query = build_query(model_class.id)

    # with cursor condition
    if cursor and is_desc:
        query = query.filter(model_class.id < cursor)
    else:
        query = query.filter(model_class.id > cursor)

    # order
    if is_desc:
        query = query.order_by(model_class.id.desc())
    else:
        query = query.order_by(model_class.id.asc())

    # filter
    if filter_func:
        query = filter_func(query)

    ids = [id for id, in query.limit(limit)]

    return ids, cursor


def cursor_query(model_class, filter_func=None, **kwargs):
    cursor = kwargs.get('cursor', 0)
    limit = kwargs.get('limit', 10)
    order = kwargs.get('order', 'desc')
    is_desc = order != 'asc'

    ids, cursor = fetch_ids_with_cursor(model_class, filter_func, **kwargs)

    # not found ids
    if not ids:
        return [], 0

    # TODO: from cache
    data = build_query(model_class).filter(model_class.id.in_(ids)).all()

    if len(data) < limit:
        return data, 0

    cursor = data[0].id if is_desc else data[-1].id
    return data, cursor


def iter_items_with_users(items, users=None):
    if not users:
        data = User.get_all([o.user_id for o in items])
        users = {o.id: o for o in data}

    for item in items:
        data = item.to_dict()
        user = users.get(item.user_id)

        if user:
            data['user'] = user.to_dict()
        yield data
