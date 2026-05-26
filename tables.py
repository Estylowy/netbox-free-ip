import django_tables2 as tables


class FreeIPRangeTable(tables.Table):
    """
    Tabela wyświetlająca wolne zakresy IP w prefiksie.
    """
    start = tables.Column(
        verbose_name='Pierwszy wolny adres',
        orderable=False,
    )
    end = tables.Column(
        verbose_name='Ostatni wolny adres',
        orderable=False,
    )
    count = tables.Column(
        verbose_name='Liczba adresów',
        orderable=False,
    )
    cidr = tables.Column(
        verbose_name='Zakres CIDR (jeśli możliwy)',
        orderable=False,
    )

    class Meta:
        attrs = {
            'class': 'table table-hover object-list',
            'id': 'free-ip-ranges-table',
        }
        empty_text = 'Brak wolnych adresów IP w tym prefiksie.'
        fields = ('start', 'end', 'count', 'cidr')
        sequence = ('start', 'end', 'count', 'cidr')
