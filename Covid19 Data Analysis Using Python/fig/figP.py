def LD_line(fig,data, ST_date, AF_date):
    fig.add_shape(
        dict(
        type = 'line',
        x0 = ST_date,
        y0 = 0,
        x1 = ST_date,
        y1 = data['Daily New Cases'].max(),
        line = dict(color='red', width = 2)
        )
    )

    fig.add_annotation(
        dict(
        x = ST_date,
        y = data['Daily New Cases'].max(),
        text = 'Starting date of curfew'
        )
    )

    fig.add_shape(
        dict(
        type = 'line',
        x0 = AF_date,
        y0 = 0,
        x1 = AF_date,
        y1 = data['Daily New Cases'].max(),
        line = dict(color='Yellow', width = 2)
        )
    )

    fig.add_annotation(
        dict(
        x = AF_date,
        y = data['Daily New Cases'].max(),
        text = 'One month later of curfew'
        )
    )

    fig.show()
