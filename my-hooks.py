# vim my-hooks.py
# Change the zap_ajax_spider target to hit dashboard hash 
# Change the crawl_depth to 2
# https://www.zaproxy.org/docs/docker/scan-hooks/
def zap_ajax_spider(zap, target, max_time):
  zap.ajaxSpider.set_option_max_crawl_depth(2)
  return zap, target + '#/dashboard', max_time