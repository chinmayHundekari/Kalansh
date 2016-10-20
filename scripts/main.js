var editable_title = $('#editable_title')
var editable_note = $('#editable_note')

editable_title.on('input', function() {
  return filter_newlines(editable_title);
});


function filter_newlines(div) {
    var node, prev, _i, _len, _ref, _results;
    prev = null;
    _ref = div.contents();
    _results = [];
    for (_i = 0, _len = _ref.length; _i < _len; _i++) {
      node = _ref[_i];
      if (node.nodeType === 3) {
        node.nodeValue = node.nodeValue.replace('\n', '');
        if (prev) {
          node.nodeValue = prev.nodeValue + node.nodeValue;
          $(prev).remove();
        }
        _results.push(prev = node);
      } else if (node.tagName.toLowerCase() === 'br') {
        _results.push($(node).remove());
      } else {
        $(node).css('display', 'inline');
        filter_newlines($(node));
        _results.push(prev = null);
      }
    }
    return _results;
  }

