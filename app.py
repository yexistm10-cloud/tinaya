import io
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Excel Merge App", page_icon="📊", layout="wide")

st.title("📊 Excel 파일 취합 도구")
st.markdown("여러 개의 Excel 파일을 업로드하면, 첫 번째 시트의 데이터를 한 번에 합쳐서 다운로드할 수 있습니다.")

st.sidebar.header("사용 방법")
st.sidebar.info(
    "1. Excel 파일을 업로드하세요.\n"
    "2. 취합 버튼을 누르세요.\n"
    "3. 결과를 미리보고 다운로드하세요."
)

uploaded_files = st.file_uploader(
    "엑셀 파일을 선택하세요 (.xlsx, .xls)",
    type=["xlsx", "xls"],
    accept_multiple_files=True,
)

if uploaded_files:
    st.success(f"{len(uploaded_files)}개 파일이 업로드되었습니다.")

    if st.button("취합 시작"):
        frames = []
        errors = []

        with st.spinner("엑셀 파일을 읽는 중입니다..."):
            for uploaded_file in uploaded_files:
                try:
                    file_name = uploaded_file.name
                    file_bytes = uploaded_file.getvalue()

                    if not file_bytes:
                        errors.append(f"{file_name}: 빈 파일입니다.")
                        continue

                    df = pd.read_excel(io.BytesIO(file_bytes), sheet_name=0)

                    if df.empty:
                        errors.append(f"{file_name}: 데이터가 없습니다.")
                        continue

                    df = df.copy()
                    df["출처 파일명"] = file_name
                    frames.append(df)

                except Exception as e:
                    errors.append(f"{uploaded_file.name}: 읽기 실패 - {e}")

        if frames:
            merged_df = pd.concat(frames, ignore_index=True, axis=0)

            st.success("취합이 완료되었습니다.")
            st.subheader("미리보기")
            st.dataframe(merged_df.head(10), use_container_width=True)

            st.subheader("다운로드")
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine="openpyxl") as writer:
                merged_df.to_excel(writer, index=False, sheet_name="취합결과")
            output.seek(0)

            st.download_button(
                label="merged_data.xlsx 다운로드",
                data=output.getvalue(),
                file_name="merged_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )

            st.caption(f"총 {len(merged_df)}개 행이 취합되었습니다.")
        else:
            st.warning("취합할 수 있는 데이터가 없습니다. 업로드 파일을 확인해 주세요.")

        if errors:
            st.warning("다음 파일은 건너뛰었습니다:")
            for msg in errors:
                st.write(f"- {msg}")
else:
    st.info("엑셀 파일을 업로드해 주세요.")
