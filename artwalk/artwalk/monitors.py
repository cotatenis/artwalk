from spidermon import Monitor, MonitorSuite, monitors
from spidermon.contrib.actions.discord.notifiers import SendDiscordMessageSpiderFinished
from spidermon.contrib.monitors.mixins import StatsMonitorMixin, ValidationMonitorMixin
from spidermon.contrib.scrapy.monitors import ItemCountMonitor, FinishReasonMonitor, UnwantedHTTPCodesMonitor
from artwalk.actions import CloseSpiderAction
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import NotConfigured
@monitors.name("Periodic job stats monitor")
class PeriodicJobStatsMonitor(Monitor, StatsMonitorMixin):
    @monitors.name("Maximum number of errors exceeded")
    def test_number_of_errors(self):
        accepted_num_errors = 5
        num_errors = self.data.stats.get("log_count/ERROR", 0)

        msg = "The job has exceeded the maximum number of errors"
        self.assertLessEqual(num_errors, accepted_num_errors, msg=msg)

@monitors.name("SKU validation")
class SkuValidationMonitor(Monitor, ValidationMonitorMixin):
    @monitors.name("Maximum sku missing")
    def test_maximum_sku_missing(self):
        self.check_missing_required_fields_percent(field_names=['productReference', 'url'], allowed_percent=0.10)

@monitors.name('Item count')
class ItemCountMonitor(Monitor):

    @monitors.name('Minimum items extracted')
    def test_minimum_number_of_items_extracted(self):
        settings = get_project_settings()
        spider_name = self.data.spider.name
        minimum_threshold_config = settings.get("SPIDERMON_CUSTOM_MIN_ITEMS")
        if minimum_threshold_config:
            minimum_threshold = minimum_threshold_config.get(spider_name)
            item_extracted = getattr(self.data.stats, 'item_scraped_count', 0)
            self.assertFalse(
                item_extracted < minimum_threshold,
                msg='Extracted less than {} items'.format(minimum_threshold)
            )
        else:
            raise NotConfigured("SPIDERMON_CUSTOM_MIN_ITEMS was not correctly loaded.")

class PeriodicMonitorSuite(MonitorSuite):
    monitors = [PeriodicJobStatsMonitor]
    monitors_failed_actions = [CloseSpiderAction, SendDiscordMessageSpiderFinished]


class SpiderCloseMonitorSuite(MonitorSuite):
    monitors = [ItemCountMonitor, SkuValidationMonitor, FinishReasonMonitor, UnwantedHTTPCodesMonitor, PeriodicJobStatsMonitor]

    monitors_failed_actions = [SendDiscordMessageSpiderFinished]