from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Memo
from .forms import MemoForm

@login_required
def memo_list(request):
	memos = Memo.objects.filter(author=request.user).order_by('-created_at')
	return render(request, 'memos/memo_list.html', {'memos': memos})

@login_required
def memo_detail(request, pk):
	memo = get_object_or_404(Memo, pk=pk, author=request.user)
	return render(request, 'memos/memo_detail.html', {'memo': memo})

@login_required
def memo_create(request):
	if request.method == 'POST':
		form = MemoForm(request.POST)
		if form.is_valid():
			memo = form.save(commit=False)
			memo.author = request.user
			memo.save()
			messages.success(request, '메모가 저장되었습니다.')
			return redirect('memo_detail', pk=memo.pk)
		else:
			messages.error(request, '입력값을 확인해 주세요.')
	else:
		form = MemoForm()
	return render(request, 'memos/memo_form.html', {'form': form})

@login_required
def memo_edit(request, pk):
	memo = get_object_or_404(Memo, pk=pk, author=request.user)
	if request.method == 'POST':
		form = MemoForm(request.POST, instance=memo)
		if form.is_valid():
			form.save()
			messages.success(request, '메모가 수정되었습니다.')
			return redirect('memo_detail', pk=memo.pk)
		else:
			messages.error(request, '입력값을 확인해 주세요.')
	else:
		form = MemoForm(instance=memo)
	return render(request, 'memos/memo_form.html', {'form': form})

@login_required
def memo_delete(request, pk):
	memo = get_object_or_404(Memo, pk=pk, author=request.user)
	if request.method == 'POST':
		memo.delete()
		messages.info(request, '메모가 삭제되었습니다.')
		return redirect('memo_list')
	return render(request, 'memos/memo_confirm_delete.html', {'memo': memo})
