from scrapers.scrape_dates import parse_date

def test_dates():
    date_tests = [
        ('20. März 2020 15.00 Uhr',             '2020-03-20T15:00'),
        ('21. März 2020, 10 Uhr',               '2020-03-21T10:00'),
        ('21. M&auml;rz 2020, 11:00 Uhr',       '2020-03-21T11:00'),
        ('21.03.2020, 15h30',                   '2020-03-21T15:30'),
        ('21. März 2020, 8.00 Uhr',             '2020-03-21T08:00'),
        ('21.&nbsp;März 2020, 18.15&nbsp; Uhr', '2020-03-21T18:15'),
        ('21. März 2020, 18.15  Uhr',           '2020-03-21T18:15'),
        ('21. März 2020, 14.00 Uhr',            '2020-03-21T14:00'),
        ('23. M&auml;rz 2020, 15 Uhr',          '2020-03-23T15:00'),
        ('18. April 2020,16.00 Uhr',            '2020-04-18T16:00'),
        ('21. März 2020',                       '2020-03-21T'),
        ('21.3.20',                             '2020-03-21T'),
        ('20.3.2020, 16.30',                    '2020-03-20T16:30'),
        ('21.03.2020, 15h30',                   '2020-03-21T15:30'),
        ('23.03.2020, 12:00',                   '2020-03-23T12:00'),
        ('23.03.2020 12:00',                    '2020-03-23T12:00'),
        ('08.04.2020: 09.30 Uhr',               '2020-04-08T09:30'),
        ('07.04.2020 15.00h',                   '2020-04-07T15:00'),
        ('31.03.20, 08.00 h',                   '2020-03-31T08:00'),
        ('20.03.2020',                          '2020-03-20T'),
        ('21 mars 2020 (18h)',                  '2020-03-21T18:00'),
        ('1er avril 2020 (16h)',                '2020-04-01T16:00'),
        ('21 mars 2020',                        '2020-03-21T'),
        ('6avril2020',                          '2020-04-06T'),
        ('20.03 à 8h00',                        '2020-03-20T08:00'),
        ('23.03 à 12h',                         '2020-03-23T12:00'),
        ('21 marzo 2020, ore 8.00',             '2020-03-21T08:00'),
        ('27.03.2020 ore 08:00',                '2020-03-27T08:00'),
        ('2020-03-23',                          '2020-03-23T'),
        ('24.3. / 10h',                         '2020-03-24T10:00'),
        ('2020-03-23T15:00:00',                 '2020-03-23T15:00'),
        ('2020-03-23 15:00:00',                 '2020-03-23T15:00'),
        ('2020-03-23 15:00',                    '2020-03-23T15:00'),
        ('30.04.2020,13.30 Uhr',                '2020-04-30T13:30'),
        ('1.Mai 2020',                          '2020-05-01T'),
        ('05-05-2020 00:00',                    '2020-05-05T00:00'),
    ]
    for text, date in date_tests:
        assert parse_date(text) == date, f"parse_date('{text}') = '{parse_date(text)}', but expected '{date}'"

if __name__ == "__main__":
    test_dates()   
