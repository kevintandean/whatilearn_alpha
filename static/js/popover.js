/**
 * Created by kevin on 7/12/2014.
 */
$('[rel=popover]').popover({
    html:true,
    placement:'right',
    content:function(){
        return $($(this).data('contentwrapper')).html();
    }
});