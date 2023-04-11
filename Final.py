import idaapi
import idautils
import ida_funcs

def breakpoint_delete(subroutine):
    idaapi.del_bpt(subroutine)

v = idaapi.simplecustviewer_t()
v.Create('Execution Trail')
def condition_function(subroutine):
    idc.set_color(subroutine, CIC_FUNC, 0x5FDFC6) 
    func_name = ida_funcs.get_func_name(subroutine)
    f = open("DebugProgress.txt", "a") 
    f.write(str(func_name)+'\n')
    f.close()
    v.AddLine("Function called is: %s" % func_name)
    v.Show()
    breakpoint_delete(subroutine)

def bind(subroutine, condition):    
    idaapi.add_bpt(subroutine,4,BPT_DEFAULT)
    breakpoint = idaapi.bpt_t()
    idaapi.get_bpt(subroutine,breakpoint)
    breakpoint.elang ='Python'
    breakpoint.condition = condition
    idaapi.update_bpt(breakpoint)

def main():
    open('DebugProgress.txt', 'w').close()
    for subroutine in idautils.Functions():
        bind(subroutine,'condition_function('+str(subroutine)+')')

main()
