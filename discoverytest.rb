require 'clearbit'
require 'json'

Clearbit.key = '95aa9a8ffe61dc6853b56a4f6f8a47b8'

targets = Clearbit::CompanySearch.search(
  {tech: 'marketo', raised: '100000~'},
  sort: 'alexa_asc'
)

puts targets.inspect