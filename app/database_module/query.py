from app import db

def column_windows(session, column, windowsize):
    def int_for_range(start_id, emd_id):
        if end_id:
            return db.and_(
                column>=start_id,
                column<end_id
            )
        else:
            return column>=start_id

    q = session.query(column, db.func.row_number().\
                              over(order_by=column).\
                              label('rownum')
                     ).\
                     from_self(column)
    if windowsize > 1:
        q = q.filter(sqlalchemy.text("rownum %% %d=1" % windowsize))

    intervals = [id for id, in q]

    while intervals:
        start = intervals.pop(0)
        if intervals:
            end = intervals[0]
        else:
            end = None
        yield int_for_range(start, end)

def windowed_query(q, column, windowsize):
    for whereclause in column_windows(q.session, column, windowsize):
        for row in q.filter(whereclause).order_by(column):
            yield row
