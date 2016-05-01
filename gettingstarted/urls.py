from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.templates.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]

configure do
  I18n.enforce_available_locales = true
  I18n.load_path = Dir[File.join(settings.root, 'locales', '*.yml')]
  I18n.backend.load_translations
  I18n.default_locale = :en
end

before do
  I18n.locale = I18n.default_locale
end

before '/:locale/*' do
  locale = params[:locale].to_sym
  if locale != I18n.default_locale && I18n.available_locales.include?(locale)
    I18n.locale = locale
    request.path_info = '/' + params[:splat][0]
  end
end

get '/' do
  erb :home
end

TOC = %w(codebase dependencies config backing-services build-release-run processes port-binding concurrency disposability dev-prod-parity logs admin-processes)

get '/:factor' do |factor|
  halt 404 unless TOC.include?(factor)
  @factor = factor
  erb :factor
end

helpers do
  def render_markdown(file)
    markdown = File.read("content/#{I18n.locale}/#{file}.md", :encoding => 'utf-8')
    Maruku.new(markdown).to_html
  rescue Errno::ENOENT
    puts "No content for #{I18n.locale}/#{file}, skipping"
  end


not_found do
  "Page not found"
end
