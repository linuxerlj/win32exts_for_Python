
import win32exts

win32exts.load_sym("*", "*")
ax = win32exts.co_create_object("vb6com.vb6test")
print win32exts.co_list_sym(ax)

# Function up_str(ByVal x As String, ByRef a As String) As Long



# ͨ���Դ�ֵ��ʽ���ã����޷���ȡ�޸ĺ�Ĳ������
print win32exts.va_invoke(ax, "up_str", "e", "abcd")



# up_str() ��2������ �����÷�ʽ����
win32exts.co_push_start()
win32exts.push_bstr("e")
win32exts.push_bstr("abcd")
i = win32exts.co_convert_by_ref()     #�����ò��������÷�ʽ����
print win32exts.co_invoke(ax, "up_str")

# ��ȡ�޸Ĺ��Ĳ���ֵ
print win32exts.co_get_by_ref(i)
