from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, QueryDict
from .models import Cursus,Student,Presence
from .form import StudentForm, PresenceForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.utils import encoding


#def index(request):
#  return HttpResponse("Racine de lycee")

# index : utilisation de HttpResponse
#def index(request):
#  result_list = Cursus.objects.order_by('name')
#  # chargement du template
#  template = loader.get_template('lycee/index.html')
#  # contexte
#  context = { 'liste' : result_list}
#  return HttpResponse(template.render(context, request))

# index : variante avec template intEgrE
def index (request):
  result_list = Cursus.objects.order_by('name')
  # contexte
  context = { 'liste' : result_list}
  # utilisation du template intEgrE
  return render (request, 'lycee/index.html', context)

def detail(request, cursus_id):
		#resp = "result for cursus {}".format(cursus_id)
		#return HttpResponse(cursus_name)
		
		result_list = Student.objects.all().filter(cursus=cursus_id)

		current_cursus = get_object_or_404(Cursus, pk=cursus_id)
		
		# contexte
		context = { 'cursus': current_cursus, 'liste' : result_list }
		return render (request, 'lycee/detail.html' , context)
		
def detail_student(request,student_id):
    #result_list = Student.objects.get(pk=student_id)
    result_list = get_object_or_404(Student, pk=student_id)
    # context
    context = {'liste': result_list,}
    return render (request, 'lycee/student/detail_student.html' , context)

def cursusCallOf(request, cursus_id):		
		result_list = Student.objects.all().filter(cursus=cursus_id)
		cursus = get_object_or_404(Cursus, pk=cursus_id)
		
		# contexte
		context = { 'liste' : result_list, 'cursus'	: cursus}
		return render (request, 'lycee/cursus_call.html' , context)

def cursusCallOfTreatment(request):
	
	stringList = str(request)
	#calendrier = stringRequest.parse
	
#	if request.method == 'POST':
	#QDrequest = QueryDict.__init__(request.body)
	"""students_missing = list(QDrequest.items())
		for student_var in students_missing:
			presence = Presence(isMissing=True, student=student_var)
			presence.full_clean()
			presence.save()

		#all_presences = presence.objects.all()
		# contexte"""
	#context = { 'liste' : QDrequest}
	"""return render (request, 'lycee/detail_calls.html' , context)
	#data = json.loads(request.body.decode('utf-8'))"""
	return HttpResponse(stringList)

class ParticularPresenceCreateView(CreateView):
  # ref au modEle
  model = Presence
  # ref au formulaire
  form_class = PresenceForm
  # le nom du render
  template_name = "lycee/presence/create_presence.html"

  # page appelEe si creation ok
  def get_success_url(self):
    return reverse ("details_presence")

def DetailPresence(request):
		result_list = Presence.objects.all()
		# context
		context = {'liste': result_list}
		return render (request, 'lycee/presence/detail_presence.html' , context)

class StudentCreateView(CreateView):
  # ref au modEle
  model = Student
  # ref au formulaire
  form_class = StudentForm
  # le nom du render
  template_name = "lycee/student/create.html"

  # page appelEe si creation ok
  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))

class EditStudentView(UpdateView):
  # ref au modEle
  model = Student
  # ref au formulaire
  form_class = StudentForm
  # le nom du render
  template_name = "lycee/student/edit_student.html"

  # page appelEe si creation ok
  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))