import streamlit as st

def main():
    st.title("简单的测试网页")
    
    # 在页面上添加文本
    st.write("欢迎使用简单的测试网页！")
    
    # 添加一个输入框，接收用户的输入
    user_input = st.text_input("请输入一些文本：")
    
    # 当用户输入时，显示用户输入的内容
    if user_input:
        st.write("你输入的内容是:", user_input)
    
    # 添加一个滑动条，接收用户的选择
    slider_value = st.slider("选择一个值：", 0, 100, 50)
    st.write("你选择的值是:", slider_value)
    
    # 添加一个按钮，点击按钮时执行操作
    if st.button("点击我！"):
        st.write("你点击了按钮！")
    
if __name__ == "__main__":
    main()
