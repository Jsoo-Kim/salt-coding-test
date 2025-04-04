# 사용자에게 폴더명 입력 받기
read -p "👤 이름(최상위 폴더명)을 입력하세요: " user_folder

# 플랫폼 별 폴더 존재 시 이동
for platform in "백준" "프로그래머스"; do
  if [ -d "$platform" ]; then
    mkdir -p "$user_folder/$platform"
    mv "$platform"/* "$user_folder/$platform/"
    rm -rf "$platform"
    echo "✅ $platform 폴더를 $user_folder/$platform 으로 이동했습니다."
  else
    echo "ℹ️ $platform 폴더가 존재하지 않아 생략했습니다."
  fi
done

# Git add까지만 자동으로 수행
if git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
  git add .
  echo "📂 변경된 파일을 git staging 영역에 추가했습니다."
  echo "✍ 이제 직접 커밋 메시지를 작성하고 아래 명령을 실행하세요:"
  echo ""
  echo "    git commit -m \"<커밋 메시지>\""
  echo "    git push origin <브랜치명>"
else
  echo "⚠️ 현재 디렉토리는 git 저장소가 아닙니다. git init 또는 clone 여부 확인하세요."
fi