%#template of the form for a new task
% rebase('base.tpl')
<p>Add a new task to the ToDo list:</p>
<form action="/new" method="post">
  <p><input type="text" size="100" maxlength="100" name="task"></p>
  <p><input type="submit" name="save" value="save"></p>
</form>