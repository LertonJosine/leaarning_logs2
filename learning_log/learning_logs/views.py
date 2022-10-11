from django.shortcuts import render
from learning_logs.models import Topic, Entry
from django.shortcuts import render
from learning_logs.forms import EntryForm,TopicForm
from django.http import HttpResponseRedirect
from django.urls import reverse
def home(request):
    return render(request, 'index.html')

def topics(request):
    topics = Topic.objects.all()
    context = {
        'topics': topics
    }

    return render(request, 'topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.all().order_by('-date_added')  # type: ignore

    context = {
        'topic': topic,
        'entries': entries
    }
    return render(request, 'topic.html', context)


def new_topic(request):
    if request.method == 'GET':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
    context = {
        'form': form
    }
    return render(request, 'new_topic.html', context)

    
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method == 'GET':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    
    context = {
        'topic': topic,
        'form':form
    }

    return render(request, 'new_entry.html', context)

def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method == 'GET':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form_edited = form.save(commit=False)
            form_edited.topic = topic
            form_edited.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))  # type: ignore
    context ={
        'form': form,
        'entry': entry
    }
    return render(request, 'edit_entry.html', context)

