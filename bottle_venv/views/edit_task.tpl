%#template for editing a task
%#the template expects to receive a value for "number" as well a "old", the text of the selected ToDo item
% rebase('base.tpl')
<p>Edit the task with ID = {{number}}</p>
<form action="/edit/{{number}}" method="post">
  <p>
  <input type="text" name="task" value="{{current_data[0]}}" size="100" maxlength="100">
  <select name="status">
    <option>open</option>
    <option>closed</option>
  </select>
  </p>
  <p><input type="submit" name="save" value="save"></p>
</form>