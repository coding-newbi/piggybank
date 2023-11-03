$(document).ready(function() {
    // Change event handler for the district dropdown
    $("#id_district").change(function() {
        var district_id = $(this).val();
        $.ajax({
            url: '{% url "load_branch" %}',  // Use the URL pattern name from your urls.py
            data: { district_id: district_id },
            dataType: 'json',
            method: 'get',
            success: function(data) {
                var branchSelect = $("#id_branch");
                branchSelect.empty();
                $.each(data.branches, function(index, branch) {
                    branchSelect.append($('<option>', {
                        value: branch.id,
                        text: branch.name
                    }));
                });
            }
        });
    });
});
