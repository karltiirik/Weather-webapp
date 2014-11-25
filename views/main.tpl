<h1>Hi, {{ip}}, {{desc}} in {{loc}}</h1>
<table align="left" border="1" cellpadding="5" cellspacing="5">
%for row in rows:
    <tr>
        <td><b>{{row[0]}}</b></td>
        <td>{{row[1]}} {{row[2]}}</td>
    </tr>
%end
</table>