# win32exts_for_Python
Win32exts_for_Python is a useful extension tool that allows you to call any 
    Win32 API or User Export API or COM/AcriveX component in Python.

======================================

# ��ӭʹ�� win32exts ������ �ⲿ��̽ӿ���չ

**�ű�����ͨ��Win32 FFI����������**


![markdown](https://www.mdeditor.com/images/logos/markdown.png "markdown")


һֱϣ����������һ��ͳһ�����Ľű����ԣ�
��ӵ�нű����ԵĶ�̬����ִ����������ӵ�нӽ���C/C++���Ч��ִ��Ч�ʣ�ͬʱ��������C/C++����������԰�ǿ��Ĺ��ܣ�����ֱ�ӵ���ϵͳ���ܡ����Ըɾ��������ӹ���ģ���ḻ��ʣ�ͬʱ��ΪǶ��ʽ�ű�Ҳ�ܵ���Ӧ�֡�
**��ϧû�У�**
������������lua, js, vbs, Python, PowerShell �������ٴ���һЩ���⡣PowerShell �﷨���ڹ��죬���ӽ���һ����ǿ���������ű���Js/vbs/lua ʹ�÷��㣬��ԭ�����ܽ�����Pythonӵ��ǿ��ĵ������⣬����������鷳��
���ǣ������˴�ǧ���硢ܿܿ�������������Եĸ����ɧ��


## �Թ�������

�����ڿ��������и������Ծ��нӴ�����Ȼ������Python��Lua���Ͼ���ΪǶ��ʽ�ű��ǳ����ʣ�������������ǰ�������ǣ�ĳ�������ض�ƽ̨����Ҫֱ�ӵ���ϵͳAPI����ʵ��ĳЩ���ܵ����⡣
��Ȼ���������Զ����ṩһЩ�ⲿ������չ��FFI���ķ�ʽ��ͨ������Ҫ�Լ���дһ��ģ��(DLL)���߶���Ľű��������е���׾�����Դ˴�ֻ����һ���������д̫��������⣬ʵ��ͳһ��������ϵͳAPI�Ļ��ơ�
**Ŀǰ��Ҫ���е������У�����һЩFFI֧�ֿ⣺**


![Pandao editor.md](https://pandao.github.io/editor.md/images/logos/editormd-logo-180x180.png "Pandao editor.md")

������չ���﷨���켫�󣬲�����Щ��Ҫ�����Ӵ�������֧�ֿ⣬��Щ�����ּ�Ϊ���ԣ�������Ӧ��Ϊ���ӵĺ������ã����͵���EnumWindows����ص��ģ��Լ����������������Ŀ�ȵĵ��ã���

��ˣ����߿�����win32exts��չ���ּ��ı��һ��**�����򵥵�**(һ��ģ��)��**ͳһ��**(���ֽű����﷨����һ��)��**��Ч��**��**����ǿ��**��(ԭ��API,COM,C++��COM�ӿڳ�Ա��֧��)ģʽ��

**һ�仰������ win32exts������ʵ�� Do whatever you want����֮�ĺ�����׼��Ҳ��**


### ��PythonΪ��(����������ʵ��೤һ������)��
### win32exts���õĻ����÷����£�

��1�����������������MessageBoxA/WΪ�������ã�

����ģ����š���һ������Ϊ�����ص�ģ���������Դ�·��������"*"��ʾ��ǰ���̵�����ģ�飻
�ڶ���������ʾ�����������ƣ�����"*"��ʾ��ģ������з��š�
win32exts.load_sym("*", "*")
�� win32exts.load_sym("C:\\windows\\system32\\user32.dll", "MessageBoxW")
�� win32exts.load_sym("user32", "MessageBoxA")
�� win32exts.load_sym("user32", "*")

win32exts.MessageBoxA(0, "call MessageBoxA", "", 1)
���ַ���Ҫ�� win32exts.L() ��װ����C/C++��ͬ��
win32exts.MessageBoxW(0, win32exts.L("call MessageBoxW"), None, 1)

��2�����ص��ĺ�������EnumWindowsΪ�������ã�

�ȷ���һ���ڴ�����ã�
	g_buf = win32exts.malloc(2*260)

����һ���ص�������
	
	
	def EnumWndProc(args):   
		��argsΪ������������ȡ������
		hWnd = win32exts.arg(args, 1)
		lParam = win32exts.arg(args, 2)
		
		win32exts.GetWindowTextW(hWnd, g_buf, 260)
		����ȡ�ڴ��еĿ��ַ�����
		��read_***ϵ�нӿڶ��ڴ棬write_***ϵ�нӿ�д�ڴ桿
		strText = win32exts.read_wstring(g_buf, 0, -1)
	
		win32exts.MessageBoxW(0, win32exts.L(strText), g_buf, 1)

		strRetVal = "1, 8"
		g_index = g_index + 1
		if g_index > 3:   ������ֻ�������Ρ�
			strRetVal = "0, 8"
	
		������ֵ�������������ַ���: "�ص�����ֵ, �����ֽ���",
		���� cdecl ����Լ���������ֽ�������ȡ 0 ��
		return strRetVal

Ȼ����ã�
	win32exts.EnumWindows(win32exts.callback("EnumWndProc"), 0)

win32exts.callback�������ڰ�װһ��Python�ص�������
����js/lua �ȵ�������˵��û���ṩ�ú�����ֱ�Ӵ��뼴�ɣ��༴��
	win32exts.EnumWindows(EnumWndProc, 0)

��3���������Ǿ������������ã�

����ͨ��ĳ���ӿڻ�ȡ��ĳ�����ĵ�ַ lFuncAddr��Ȼ���������������ʽ���ã�

	win32exts.push_value(arg1)     ��������������
	win32exts.push_wstring("arg2") �������ǿ��ַ�����
	win32exts.push_astring(arg3)   �������Ƕ��ֽ��ַ�����
	win32exts.push_double(arg4)    ��������˫���ȸ�������
	win32exts.push_float(arg5)     �������ǵ����ȸ�������
	iRetVal = win32exts.call( lFuncAddr )

��Ȼ��������Ҳ�������Ƶ��ã����磺
	win32exts.push_value(0)
	win32exts.push_astring("Py_MessageBoxA_V1")
	win32exts.push_value(0)
	win32exts.push_value(0)
	iRetVal = win32exts.sym_call("MessageBoxA")  ������ func_call��


# ʵ�ڱ಻��ȥ�ˣ���___��b'���������win32exts�ṩͳһ���ýӿ��嵥��һ��, ���ڵ����÷���ο�git�ϵ� win32exts_for_Xxxx �ֿ��demo ʾ����

