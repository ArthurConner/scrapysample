from datetime import datetime

class TidyUp(object):
	def process_item(self, item, spider):
		datetime_object = datetime.strptime(item['piece_date'][0], '%A, %B %d, %Y')
		item['date'] = datetime_object.isoformat()  # map(datetime.isoformat, datetime_object)
		return item
