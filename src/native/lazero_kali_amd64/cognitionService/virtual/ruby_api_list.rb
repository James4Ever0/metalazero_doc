require 'solargraph'

api_map = Solargraph::ApiMap.new
pins = api_map.get_methods('String')
print(pins)
