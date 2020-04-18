from django_components import component

class Example(component.Component):
    def context(self, date):
        return {
            "txt": txt,
            "date": date
        }

    def template(self, date, txt):
        return "imgClassifier/components/Example/example.html"

    class Media:
        css = {'all': ['imgClassifier/components/Example/example.css']}
        js = ['imgClassifier/components/Example/example.js']

component.registry.register(name="example", component=Example)