$(function () {
  const searchButton = $("#search_button");

  // Handle clicks of the Search button and the Enter key
  searchButton.click(doSearch);
  $('#search_form').submit(doSearch);

  // Search the videos that were indexed
  function doSearch(e) {
    e.stopPropagation();
    e.preventDefault();

    searchButton.prop('disabled', true);
    const query = $("#search_box").val();

    fetch(`/search?query=${query}`).then(function (response) {
      return response.json();
    }).then(function (data) {
      let innerHtml = "";
      // Populate search results
      data.results.forEach(function (entry) {
        innerHtml = innerHtml + '<div class="tile"><div class="title">' + entry.name + '</div><div class="video-image"><img class="thumbnail" src="/thumbnail?id=' + entry.thumbnailId + '&videoId=' + entry.thumbnailVideoId + '" /></div>';
        innerHtml = innerHtml + '<div class="table">';

        // Add an entry for each search hit
        entry.searchMatches.forEach(function (match) {
          innerHtml = innerHtml + '<div class="row">';
          innerHtml = innerHtml + '<div class="cell">';
          innerHtml = innerHtml + '<img src="/public/images/icon-' + match.type + '.png" />';
          innerHtml = innerHtml + '</div>';
          innerHtml = innerHtml + '<div class="cell" style="width:36vw">';
          innerHtml = innerHtml + match.text.replace(match.exactText, '<span class="match">' + match.exactText + '</span>');
          innerHtml = innerHtml + '<span style="font-weight:bold"> (' + match.startTime.split('.')[ 0 ] + ')</span>';
          innerHtml = innerHtml + '</div>';
          innerHtml = innerHtml + '</div>';
        });

        innerHtml = innerHtml + '</div>';
        innerHtml = innerHtml + '</div>';
      });

      $('#searchResults').html(innerHtml);
    }).catch(function (err) {
      alert(err);
    });
    searchButton.prop('disabled', false);
  }
});
