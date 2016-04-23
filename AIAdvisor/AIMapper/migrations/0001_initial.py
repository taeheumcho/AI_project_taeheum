# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(null=True, blank=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EtfCategory',
            fields=[
                ('idx', models.AutoField(serialize=False, primary_key=True, db_column='IDX')),
                ('code', models.CharField(max_length=45, unique=True, null=True, db_column='CODE', blank=True)),
                ('name', models.CharField(max_length=255, null=True, db_column='NAME', blank=True)),
                ('crtn_time', models.DateTimeField(null=True, db_column='CRTN_TIME', blank=True)),
                ('update_time', models.DateTimeField(null=True, db_column='UPDATE_TIME', blank=True)),
            ],
            options={
                'db_table': 'etf_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EtfData',
            fields=[
                ('idx', models.AutoField(serialize=False, primary_key=True, db_column='IDX')),
                ('DT', models.CharField(max_length=8, db_column='DT')),
                ('TICKER', models.CharField(max_length=45, db_column='TICKER')),
                ('price_close', models.FloatField(null=True, db_column='PRICE_CLOSE', blank=True)),
                ('price_open', models.FloatField(null=True, db_column='PRICE_OPEN', blank=True)),
                ('price_high', models.FloatField(null=True, db_column='PRICE_HIGH', blank=True)),
                ('price_low', models.FloatField(null=True, db_column='PRICE_LOW', blank=True)),
                ('volume', models.FloatField(null=True, db_column='VOLUME', blank=True)),
                ('crtn_time', models.DateTimeField(null=True, db_column='CRTN_TIME', blank=True)),
                ('update_time', models.DateTimeField(null=True, db_column='UPDATE_TIME', blank=True)),
            ],
            options={
                'db_table': 'etf_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EtfInfo',
            fields=[
                ('idx', models.AutoField(serialize=False, primary_key=True, db_column='IDX')),
                ('ticker', models.CharField(max_length=45, unique=True, null=True, db_column='TICKER', blank=True)),
                ('name', models.CharField(max_length=255, null=True, db_column='NAME', blank=True)),
                ('category_code', models.CharField(max_length=10, null=True, db_column='CATEGORY_CODE', blank=True)),
                ('fund_family', models.CharField(max_length=90, null=True, db_column='FUND_FAMILY', blank=True)),
                ('exchange', models.CharField(max_length=10, null=True, db_column='EXCHANGE', blank=True)),
                ('country', models.CharField(max_length=10, null=True, db_column='COUNTRY', blank=True)),
                ('ccy_cd', models.CharField(max_length=10, null=True, db_column='CCY_CD', blank=True)),
                ('crtn_time', models.DateTimeField(null=True, db_column='CRTN_TIME', blank=True)),
                ('update_time', models.DateTimeField(null=True, db_column='UPDATE_TIME', blank=True)),
            ],
            options={
                'db_table': 'etf_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FuturesData',
            fields=[
                ('idx', models.AutoField(serialize=False, primary_key=True, db_column='IDX')),
                ('DT', models.CharField(max_length=8, null=True, db_column='DT', blank=True)),
                ('TICKER', models.CharField(max_length=45, null=True, db_column='TICKER', blank=True)),
                ('OVERNIGHT_CD', models.CharField(max_length=2, null=True, db_column='OVERNIGHT_CD', blank=True)),
                ('close_price', models.FloatField(null=True, db_column='CLOSE_PRICE', blank=True)),
                ('open_price', models.FloatField(null=True, db_column='OPEN_PRICE', blank=True)),
                ('high_price', models.FloatField(null=True, db_column='HIGH_PRICE', blank=True)),
                ('low_price', models.FloatField(null=True, db_column='LOW_PRICE', blank=True)),
                ('volume', models.IntegerField(null=True, db_column='VOLUME', blank=True)),
                ('settlement_price', models.FloatField(null=True, db_column='SETTLEMENT_PRICE', blank=True)),
                ('spot_price', models.FloatField(null=True, db_column='SPOT_PRICE', blank=True)),
                ('outstanding_volume', models.IntegerField(null=True, db_column='OUTSTANDING_VOLUME', blank=True)),
                ('crtn_time', models.DateTimeField(null=True, db_column='CRTN_TIME', blank=True)),
                ('update_time', models.DateTimeField(null=True, db_column='UPDATE_TIME', blank=True)),
            ],
            options={
                'db_table': 'futures_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FuturesInfo',
            fields=[
                ('idx', models.AutoField(serialize=False, primary_key=True, db_column='IDX')),
                ('ticker', models.CharField(max_length=45, unique=True, null=True, db_column='TICKER', blank=True)),
                ('name', models.CharField(max_length=255, null=True, db_column='NAME', blank=True)),
                ('short_ticker', models.CharField(max_length=45, null=True, db_column='SHORT_TICKER', blank=True)),
                ('expire_dt', models.CharField(max_length=6, null=True, db_column='EXPIRE_DT', blank=True)),
                ('spread_type', models.CharField(max_length=2, null=True, db_column='SPREAD_TYPE', blank=True)),
                ('type_cd', models.CharField(max_length=45, null=True, db_column='TYPE_CD', blank=True)),
                ('crtn_time', models.DateTimeField(null=True, db_column='CRTN_TIME', blank=True)),
                ('update_time', models.DateTimeField(null=True, db_column='UPDATE_TIME', blank=True)),
            ],
            options={
                'db_table': 'futures_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FuturesInvestor',
            fields=[
                ('idx', models.AutoField(serialize=False, primary_key=True, db_column='IDX')),
                ('DT', models.CharField(max_length=8, null=True, db_column='DT', blank=True)),
                ('TICKER', models.CharField(max_length=45, null=True, db_column='TICKER', blank=True)),
                ('OVERNIGHT_CD', models.CharField(max_length=2, null=True, db_column='OVERNIGHT_CD', blank=True)),
                ('INVESTOR_CD', models.CharField(max_length=4, null=True, db_column='INVESTOR_CD', blank=True)),
                ('buy_amount', models.FloatField(null=True, db_column='BUY_AMOUNT', blank=True)),
                ('buy_volume', models.FloatField(null=True, db_column='BUY_VOLUME', blank=True)),
                ('sell_amount', models.FloatField(null=True, db_column='SELL_AMOUNT', blank=True)),
                ('sell_volume', models.FloatField(null=True, db_column='SELL_VOLUME', blank=True)),
                ('crtn_time', models.DateTimeField(null=True, db_column='CRTN_TIME', blank=True)),
                ('update_time', models.DateTimeField(null=True, db_column='UPDATE_TIME', blank=True)),
            ],
            options={
                'db_table': 'futures_investor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FxData',
            fields=[
                ('idx', models.AutoField(serialize=False, primary_key=True, db_column='IDX')),
                ('DT', models.CharField(max_length=8, null=True, db_column='DT', blank=True)),
                ('TICKER', models.CharField(max_length=45, null=True, db_column='TICKER', blank=True)),
                ('price_close', models.FloatField(null=True, db_column='PRICE_CLOSE', blank=True)),
                ('price_open', models.FloatField(null=True, db_column='PRICE_OPEN', blank=True)),
                ('price_high', models.FloatField(null=True, db_column='PRICE_HIGH', blank=True)),
                ('price_low', models.FloatField(null=True, db_column='PRICE_LOW', blank=True)),
                ('volume', models.FloatField(null=True, db_column='VOLUME', blank=True)),
                ('crtn_time', models.DateTimeField(null=True, db_column='CRTN_TIME', blank=True)),
                ('update_time', models.DateTimeField(null=True, db_column='UPDATE_TIME', blank=True)),
            ],
            options={
                'db_table': 'fx_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FxInfo',
            fields=[
                ('idx', models.AutoField(serialize=False, primary_key=True, db_column='IDX')),
                ('ticker', models.CharField(max_length=45, unique=True, null=True, db_column='TICKER', blank=True)),
                ('name', models.CharField(max_length=255, null=True, db_column='NAME', blank=True)),
                ('ccy1', models.CharField(max_length=10, null=True, db_column='CCY1', blank=True)),
                ('ccy2', models.CharField(max_length=10, null=True, db_column='CCY2', blank=True)),
                ('crtn_time', models.DateTimeField(null=True, db_column='CRTN_TIME', blank=True)),
                ('update_time', models.DateTimeField(null=True, db_column='UPDATE_TIME', blank=True)),
            ],
            options={
                'db_table': 'fx_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IndexData',
            fields=[
                ('idx', models.AutoField(serialize=False, primary_key=True, db_column='IDX')),
                ('DT', models.CharField(max_length=8, null=True, db_column='DT', blank=True)),
                ('TICKER', models.CharField(max_length=45, null=True, db_column='TICKER', blank=True)),
                ('price_close', models.FloatField(null=True, db_column='PRICE_CLOSE', blank=True)),
                ('price_open', models.FloatField(null=True, db_column='PRICE_OPEN', blank=True)),
                ('price_high', models.FloatField(null=True, db_column='PRICE_HIGH', blank=True)),
                ('price_low', models.FloatField(null=True, db_column='PRICE_LOW', blank=True)),
                ('volume', models.FloatField(null=True, db_column='VOLUME', blank=True)),
                ('crtn_time', models.DateTimeField(null=True, db_column='CRTN_TIME', blank=True)),
                ('update_time', models.DateTimeField(null=True, db_column='UPDATE_TIME', blank=True)),
            ],
            options={
                'db_table': 'index_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IndexInfo',
            fields=[
                ('idx', models.AutoField(serialize=False, primary_key=True, db_column='IDX')),
                ('ticker', models.CharField(max_length=45, unique=True, null=True, db_column='TICKER', blank=True)),
                ('name', models.CharField(max_length=255, null=True, db_column='NAME', blank=True)),
                ('exchange', models.CharField(max_length=10, null=True, db_column='EXCHANGE', blank=True)),
                ('country', models.CharField(max_length=10, null=True, db_column='COUNTRY', blank=True)),
                ('crtn_time', models.DateTimeField(null=True, db_column='CRTN_TIME', blank=True)),
                ('update_time', models.DateTimeField(null=True, db_column='UPDATE_TIME', blank=True)),
            ],
            options={
                'db_table': 'index_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IrData',
            fields=[
                ('idx', models.AutoField(serialize=False, primary_key=True, db_column='IDX')),
                ('DT', models.CharField(max_length=8, null=True, db_column='DT', blank=True)),
                ('TICKER', models.CharField(max_length=45, null=True, db_column='TICKER', blank=True)),
                ('value1', models.FloatField(null=True, db_column='VALUE1', blank=True)),
                ('value2', models.FloatField(null=True, db_column='VALUE2', blank=True)),
                ('crtn_time', models.DateTimeField(null=True, db_column='CRTN_TIME', blank=True)),
                ('update_time', models.DateTimeField(null=True, db_column='UPDATE_TIME', blank=True)),
            ],
            options={
                'db_table': 'ir_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IrInfo',
            fields=[
                ('idx', models.AutoField(serialize=False, primary_key=True, db_column='IDX')),
                ('ticker', models.CharField(max_length=45, unique=True, null=True, db_column='TICKER', blank=True)),
                ('irc_cd', models.CharField(max_length=45, null=True, db_column='IRC_CD', blank=True)),
                ('mrty_cd', models.CharField(max_length=10, null=True, db_column='MRTY_CD', blank=True)),
                ('name', models.CharField(max_length=255, null=True, db_column='NAME', blank=True)),
                ('crtn_time', models.DateTimeField(null=True, db_column='CRTN_TIME', blank=True)),
                ('update_time', models.DateTimeField(null=True, db_column='UPDATE_TIME', blank=True)),
            ],
            options={
                'db_table': 'ir_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('idx', models.AutoField(serialize=False, primary_key=True, db_column='IDX')),
                ('DT', models.CharField(max_length=8, db_column='DT')),
                ('TICKER', models.CharField(max_length=45, db_column='TICKER')),
                ('price_close', models.FloatField(null=True, db_column='PRICE_CLOSE', blank=True)),
                ('price_open', models.FloatField(null=True, db_column='PRICE_OPEN', blank=True)),
                ('price_high', models.FloatField(null=True, db_column='PRICE_HIGH', blank=True)),
                ('price_low', models.FloatField(null=True, db_column='PRICE_LOW', blank=True)),
                ('volume', models.FloatField(null=True, db_column='VOLUME', blank=True)),
                ('amount', models.BigIntegerField(null=True, db_column='AMOUNT', blank=True)),
                ('marketcap', models.BigIntegerField(null=True, db_column='MARKETCAP', blank=True)),
                ('listed_shares', models.IntegerField(null=True, db_column='LISTED_SHARES', blank=True)),
                ('crtn_time', models.DateTimeField(null=True, db_column='CRTN_TIME', blank=True)),
                ('update_time', models.DateTimeField(null=True, db_column='UPDATE_TIME', blank=True)),
            ],
            options={
                'db_table': 'stock_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StockDetail',
            fields=[
                ('idx', models.AutoField(serialize=False, primary_key=True, db_column='IDX')),
                ('DT', models.CharField(max_length=8, null=True, db_column='DT', blank=True)),
                ('TICKER', models.CharField(max_length=45, null=True, db_column='TICKER', blank=True)),
                ('ma_200', models.FloatField(null=True, db_column='MA_200', blank=True)),
                ('ma_50', models.FloatField(null=True, db_column='MA_50', blank=True)),
                ('book_value', models.FloatField(null=True, db_column='BOOK_VALUE', blank=True)),
                ('volume_avg', models.FloatField(null=True, db_column='VOLUME_AVG', blank=True)),
                ('ebitda', models.FloatField(null=True, db_column='EBITDA', blank=True)),
                ('dividend_yield', models.FloatField(null=True, db_column='DIVIDEND_YIELD', blank=True)),
                ('market_cap', models.FloatField(null=True, db_column='MARKET_CAP', blank=True)),
                ('year_high', models.FloatField(null=True, db_column='YEAR_HIGH', blank=True)),
                ('year_low', models.FloatField(null=True, db_column='YEAR_LOW', blank=True)),
                ('crtn_time', models.DateTimeField(null=True, db_column='CRTN_TIME', blank=True)),
                ('update_time', models.DateTimeField(null=True, db_column='UPDATE_TIME', blank=True)),
            ],
            options={
                'db_table': 'stock_detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StockInfo',
            fields=[
                ('idx', models.AutoField(serialize=False, primary_key=True, db_column='IDX')),
                ('ticker', models.CharField(max_length=45, unique=True, null=True, db_column='TICKER', blank=True)),
                ('short_ticker', models.CharField(max_length=45, null=True, db_column='SHORT_TICKER', blank=True)),
                ('name', models.CharField(max_length=255, null=True, db_column='NAME', blank=True)),
                ('exchange', models.CharField(max_length=10, null=True, db_column='EXCHANGE', blank=True)),
                ('country', models.CharField(max_length=10, null=True, db_column='COUNTRY', blank=True)),
                ('ccy_cd', models.CharField(max_length=10, null=True, db_column='CCY_CD', blank=True)),
                ('data_source', models.CharField(max_length=5, null=True, db_column='DATA_SOURCE', blank=True)),
                ('crtn_time', models.DateTimeField(null=True, db_column='CRTN_TIME', blank=True)),
                ('update_time', models.DateTimeField(null=True, db_column='UPDATE_TIME', blank=True)),
            ],
            options={
                'db_table': 'stock_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StockInvestor',
            fields=[
                ('idx', models.AutoField(serialize=False, primary_key=True, db_column='IDX')),
                ('DT', models.CharField(max_length=8, null=True, db_column='DT', blank=True)),
                ('TICKER', models.CharField(max_length=45, null=True, db_column='TICKER', blank=True)),
                ('INVESTOR_CD', models.CharField(max_length=4, null=True, db_column='INVESTOR_CD', blank=True)),
                ('buy_amount', models.BigIntegerField(null=True, db_column='BUY_AMOUNT', blank=True)),
                ('buy_volume', models.IntegerField(null=True, db_column='BUY_VOLUME', blank=True)),
                ('sell_amount', models.BigIntegerField(null=True, db_column='SELL_AMOUNT', blank=True)),
                ('sell_volume', models.IntegerField(null=True, db_column='SELL_VOLUME', blank=True)),
                ('crtn_time', models.DateTimeField(null=True, db_column='CRTN_TIME', blank=True)),
                ('update_time', models.DateTimeField(null=True, db_column='UPDATE_TIME', blank=True)),
            ],
            options={
                'db_table': 'stock_investor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StockShort',
            fields=[
                ('idx', models.AutoField(serialize=False, primary_key=True, db_column='IDX')),
                ('DT', models.CharField(max_length=8, null=True, db_column='DT', blank=True)),
                ('TICKER', models.CharField(max_length=45, null=True, db_column='TICKER', blank=True)),
                ('volume', models.IntegerField(null=True, db_column='VOLUME', blank=True)),
                ('amount', models.BigIntegerField(null=True, db_column='AMOUNT', blank=True)),
                ('total_volume', models.IntegerField(null=True, db_column='TOTAL_VOLUME', blank=True)),
                ('total_amount', models.BigIntegerField(null=True, db_column='TOTAL_AMOUNT', blank=True)),
                ('total_shares', models.BigIntegerField(null=True, db_column='TOTAL_SHARES', blank=True)),
                ('crtn_time', models.DateTimeField(null=True, db_column='CRTN_TIME', blank=True)),
                ('update_time', models.DateTimeField(null=True, db_column='UPDATE_TIME', blank=True)),
            ],
            options={
                'db_table': 'stock_short',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StockSuspension',
            fields=[
                ('idx', models.AutoField(serialize=False, primary_key=True, db_column='IDX')),
                ('DT', models.CharField(max_length=8, null=True, db_column='DT', blank=True)),
                ('TICKER', models.CharField(max_length=45, null=True, db_column='TICKER', blank=True)),
                ('start_dt', models.CharField(max_length=8, null=True, db_column='START_DT', blank=True)),
                ('reason', models.CharField(max_length=255, null=True, db_column='REASON', blank=True)),
                ('crtn_time', models.DateTimeField(null=True, db_column='CRTN_TIME', blank=True)),
                ('update_time', models.DateTimeField(null=True, db_column='UPDATE_TIME', blank=True)),
            ],
            options={
                'db_table': 'stock_suspension',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='XpathData',
            fields=[
                ('idx', models.AutoField(serialize=False, primary_key=True, db_column='IDX')),
                ('code', models.CharField(max_length=45, unique=True, null=True, db_column='CODE', blank=True)),
                ('xpath_code', models.CharField(max_length=45, null=True, db_column='XPATH_CODE', blank=True)),
                ('xpath', models.CharField(max_length=255, null=True, db_column='XPATH', blank=True)),
                ('xpath_index', models.IntegerField(null=True, db_column='XPATH_INDEX', blank=True)),
                ('use', models.CharField(max_length=1, null=True, db_column='USE', blank=True)),
                ('insert_column', models.CharField(max_length=45, null=True, db_column='INSERT_COLUMN', blank=True)),
                ('description', models.CharField(max_length=255, null=True, db_column='DESCRIPTION', blank=True)),
                ('crtn_time', models.DateTimeField(null=True, db_column='CRTN_TIME', blank=True)),
                ('update_time', models.DateTimeField(null=True, db_column='UPDATE_TIME', blank=True)),
            ],
            options={
                'db_table': 'xpath_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='XpathInfo',
            fields=[
                ('idx', models.AutoField(serialize=False, primary_key=True, db_column='IDX')),
                ('code', models.CharField(max_length=45, unique=True, null=True, db_column='CODE', blank=True)),
                ('sitecode', models.CharField(max_length=10, null=True, db_column='SITECODE', blank=True)),
                ('url', models.CharField(max_length=255, null=True, db_column='URL', blank=True)),
                ('description', models.CharField(max_length=255, null=True, db_column='DESCRIPTION', blank=True)),
            ],
            options={
                'db_table': 'xpath_info',
                'managed': False,
            },
        ),
    ]
