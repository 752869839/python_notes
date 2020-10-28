# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import re
import hashlib
import htmlmin
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline,FilesPipeline
from scrapy.pipelines.files import FSFilesStore,S3FilesStore,GCSFilesStore
from scrapy.utils.python import to_bytes
from Seaweedfs.stores import WeedFilesStore
from tor_spider.sim_hash import p_id

# ImagesPipeline
class DownloadImagesPipeline(ImagesPipeline):
    STORE_SCHEMES = {
        '':FSFilesStore,
        'file': FSFilesStore,
        's3': S3FilesStore,
        'gs': GCSFilesStore,
        'weed': WeedFilesStore
    }

    def get_media_requests(self,item,info):
        try:
            for url in item['img']:
                yield Request(url, meta={'item': item})
        except:
            pass

    def file_path(self, request, response=None, info=None):
        if request.url[0:29] == 'http://agarthaangodtcz3.onion':
            item = request.meta['item']
            image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest() + '.jpg'
            index = 'page'
            domain = 'agarthaangodtcz3.onion'
            raw_text = htmlmin.minify(item['html'].encode('utf-8').decode('utf-8'), remove_all_empty_space=True)
            index_id = p_id(domain, raw_text)
            return './%s/%s/%s' % (index,index_id,image_guid)

        elif request.url[0:29] == 'http://alibaba2kw6qoh6o.onion':
            item = request.meta['item']
            image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest() + '.jpg'
            index = 'page'
            domain = 'alibaba2kw6qoh6o.onion'
            raw_text = htmlmin.minify(item['html'].encode('utf-8').decode('utf-8'), remove_all_empty_space=True)
            index_id = p_id(domain, raw_text)
            return './%s/%s/%s' % (index,index_id,image_guid)


        elif request.url[0:29] == 'http://apollonvm7uin7yw.onion':
            item = request.meta['item']
            image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest() + '.jpg'
            index = 'page'
            domain = 'apollonvm7uin7yw.onion'
            raw_text = htmlmin.minify(item['html'].encode('utf-8').decode('utf-8'), remove_all_empty_space=True)
            index_id = p_id(domain, raw_text)
            return './%s/%s/%s' % (index,index_id,image_guid)

        elif request.url[0:29] == 'http://avengersdutyk3xf.onion':
            item = request.meta['item']
            image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest() + '.jpg'
            index = 'page'
            domain = 'avengersdutyk3xf.onion'
            raw_text = htmlmin.minify(item['html'].encode('utf-8').decode('utf-8'), remove_all_empty_space=True)
            index_id = p_id(domain, raw_text)
            return './%s/%s/%s' % (index,index_id,image_guid)

        elif request.url[0:69] == 'http://c2p3hg35jalss7b2a6hkmhzflgevkonqt7g6jze62ro2g4h4wmzwobid.onion':
            item = request.meta['item']
            image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest() + '.jpg'
            index = 'page'
            domain = 'c2p3hg35jalss7b2a6hkmhzflgevkonqt7g6jze62ro2g4h4wmzwobid.onion'
            raw_text = htmlmin.minify(item['html'].encode('utf-8').decode('utf-8'), remove_all_empty_space=True)
            index_id = p_id(domain, raw_text)
            return './%s/%s/%s' % (index,index_id,image_guid)

        elif request.url[0:29] == 'http://cryptbb2gezhohku.onion':
            item = request.meta['item']
            image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest() + '.jpg'
            index = 'page'
            domain = 'cryptbb2gezhohku.onion'
            raw_text = htmlmin.minify(item['html'].encode('utf-8').decode('utf-8'), remove_all_empty_space=True)
            index_id = p_id(domain, raw_text)
            return './%s/%s/%s' % (index,index_id,image_guid)

        elif request.url[0:29] == 'http://facebookcorewwwi.onion':
            item = request.meta['item']
            image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest() + '.jpg'
            index = 'page'
            domain = 'facebookcorewwwi.onion'
            raw_text = htmlmin.minify(item['html'].encode('utf-8').decode('utf-8'), remove_all_empty_space=True)
            index_id = p_id(domain, raw_text)
            return './%s/%s/%s' % (index,index_id,image_guid)

        elif request.url[0:69] == 'http://gunsganos2raowan5y2nkblujnmza32v2cwkdgy6okciskzabchx4iqd.onion':
            item = request.meta['item']
            image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest() + '.jpg'
            index = 'page'
            domain = 'gunsganos2raowan5y2nkblujnmza32v2cwkdgy6okciskzabchx4iqd.onion'
            raw_text = htmlmin.minify(item['html'].encode('utf-8').decode('utf-8'), remove_all_empty_space=True)
            index_id = p_id(domain, raw_text)
            return './%s/%s/%s' % (index,index_id,image_guid)

        elif request.url[0:69] == 'http://gw6zzvqgy6v2czxrmphuerrtbirftvkyfkeoaiorg5qijqlsbqfpqjqd.onion':
            item = request.meta['item']
            image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest() + '.jpg'
            index = 'page'
            domain = 'gw6zzvqgy6v2czxrmphuerrtbirftvkyfkeoaiorg5qijqlsbqfpqjqd.onion'
            raw_text = htmlmin.minify(item['html'].encode('utf-8').decode('utf-8'), remove_all_empty_space=True)
            index_id = p_id(domain, raw_text)
            return './%s/%s/%s' % (index,index_id,image_guid)

        elif request.url[0:29] == 'http://horoiomuy6xignjv.onion':
            item = request.meta['item']
            image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest() + '.jpg'
            index = 'page'
            domain = 'horoiomuy6xignjv.onion'
            raw_text = htmlmin.minify(item['html'].encode('utf-8').decode('utf-8'), remove_all_empty_space=True)
            index_id = p_id(domain, raw_text)
            return './%s/%s/%s' % (index,index_id,image_guid)

        elif request.url[0:29] == 'http://24hourspkcmd7bvr.onion':
            item = request.meta['item']
            image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest() + '.jpg'
            index = 'page'
            domain = '24hourspkcmd7bvr.onion'
            raw_text = htmlmin.minify(item['html'].encode('utf-8').decode('utf-8'), remove_all_empty_space=True)
            index_id = p_id(domain, raw_text)
            return './%s/%s/%s' % (index,index_id,image_guid)

        elif request.url[0:29] == 'http://jesblogfnk2boep4.onion':
            item = request.meta['item']
            image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest() + '.jpg'
            index = 'page'
            domain = 'jesblogfnk2boep4.onion'
            raw_text = htmlmin.minify(item['html'].encode('utf-8').decode('utf-8'), remove_all_empty_space=True)
            index_id = p_id(domain, raw_text)
            return './%s/%s/%s' % (index,index_id,image_guid)

        elif request.url[0:69] == 'http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion':
            item = request.meta['item']
            image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest() + '.jpg'
            index = 'page'
            domain = 'lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion'
            raw_text = htmlmin.minify(item['html'].encode('utf-8').decode('utf-8'), remove_all_empty_space=True)
            index_id = p_id(domain, raw_text)
            return './%s/%s/%s' % (index,index_id,image_guid)

        elif request.url[0:29] == 'http://ninanyykvluxfsba.onion':
            item = request.meta['item']
            image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest() + '.jpg'
            index = 'page'
            domain = 'ninanyykvluxfsba.onion'
            raw_text = htmlmin.minify(item['html'].encode('utf-8').decode('utf-8'), remove_all_empty_space=True)
            index_id = p_id(domain, raw_text)
            return './%s/%s/%s' % (index,index_id,image_guid)

        elif request.url[0:39] == 'https://static01.graylady3jvrrxbe.onion':
            item = request.meta['item']
            image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest() + '.jpg'
            index = 'page'
            domain = 'nytimes3xbfgragh.onion'
            raw_text = htmlmin.minify(item['html'].encode('utf-8').decode('utf-8'), remove_all_empty_space=True)
            index_id = p_id(domain, raw_text)
            return './%s/%s/%s' % (index,index_id,image_guid)

        elif request.url[0:29] == 'http://pncldyerk4gqofhp.onion':
            item = request.meta['item']
            image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest() + '.jpg'
            index = 'page'
            domain = 'pncldyerk4gqofhp.onion'
            raw_text = htmlmin.minify(item['html'].encode('utf-8').decode('utf-8'), remove_all_empty_space=True)
            index_id = p_id(domain, raw_text)
            return './%s/%s/%s' % (index,index_id,image_guid)

        elif request.url[0:69] == 'http://sfdu2jstlnp7whqlzpojopr5jxehxz4dveqfl67v6mfrwoj3nq6cnrad.onion':
            item = request.meta['item']
            image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest() + '.jpg'
            index = 'page'
            domain = 'sfdu2jstlnp7whqlzpojopr5jxehxz4dveqfl67v6mfrwoj3nq6cnrad.onion'
            raw_text = htmlmin.minify(item['html'].encode('utf-8').decode('utf-8'), remove_all_empty_space=True)
            index_id = p_id(domain, raw_text)
            return './%s/%s/%s' % (index,index_id,image_guid)

        elif request.url[0:29] == 'http://shoptwgap2x3xbwy.onion':
            item = request.meta['item']
            image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest() + '.jpg'
            index = 'page'
            domain = 'shoptwgap2x3xbwy.onion'
            raw_text = htmlmin.minify(item['html'].encode('utf-8').decode('utf-8'), remove_all_empty_space=True)
            index_id = p_id(domain, raw_text)
            return './%s/%s/%s' % (index,index_id,image_guid)

        elif request.url[0:69] == 'http://torum43tajnrxritn4iumy75giwb5yfw6cjq2czjikhtcac67tfif2yd.onion':
            item = request.meta['item']
            image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest() + '.jpg'
            index = 'page'
            domain = 'torum43tajnrxritn4iumy75giwb5yfw6cjq2czjikhtcac67tfif2yd.onion'
            raw_text = htmlmin.minify(item['html'].encode('utf-8').decode('utf-8'), remove_all_empty_space=True)
            index_id = p_id(domain, raw_text)
            return './%s/%s/%s' % (index,index_id,image_guid)

        elif request.url[0:69] == 'http://xxxxxxxxxs6qbnahsbvxbghsnqh4rj6whbyblqtnmetf7vell2fmxmad.onion':
            item = request.meta['item']
            image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest() + '.jpg'
            index = 'page'
            domain = 'xxxxxxxxxs6qbnahsbvxbghsnqh4rj6whbyblqtnmetf7vell2fmxmad.onion'
            raw_text = htmlmin.minify(item['html'].encode('utf-8').decode('utf-8'), remove_all_empty_space=True)
            index_id = p_id(domain, raw_text)
            return './%s/%s/%s' % (index,index_id,image_guid)

        elif request.url[0:29] == 'http://yue4eifx522t5zjb.onion':
            item = request.meta['item']
            image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest() + '.jpg'
            index = 'page'
            domain = 'yue4eifx522t5zjb.onion'
            raw_text = htmlmin.minify(item['html'].encode('utf-8').decode('utf-8'), remove_all_empty_space=True)
            index_id = p_id(domain, raw_text)
            return './%s/%s/%s' % (index,index_id,image_guid)

        elif request.url[0:69] == 'http://7zj4oshsyhokgus6fyk7pmdiubu4mkjpjjprjkvopnhnwylr522tymqd.onion':
            item = request.meta['item']
            image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest() + '.jpg'
            index = 'page'
            domain = '7zj4oshsyhokgus6fyk7pmdiubu4mkjpjjprjkvopnhnwylr522tymqd.onion'
            raw_text = htmlmin.minify(item['html'].encode('utf-8').decode('utf-8'), remove_all_empty_space=True)
            index_id = p_id(domain, raw_text)
            return './%s/%s/%s' % (index,index_id,image_guid)