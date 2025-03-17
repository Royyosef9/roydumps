#!/bin/bash

# צבעים לפלט (אופציונלי)
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # ללא צבע

echo -e "${GREEN} בדיקה אם Docker מותקן...${NC}"
if ! command -v docker &> /dev/null; then
    echo -e "${RED}❌ Docker לא מותקן. התקן אותו ונסה שוב.${NC}"
    exit 1
fi

echo -e "${GREEN} מנקה קונטיינר קודם אם קיים...${NC}"
docker stop royapp-container &> /dev/null
docker rm royapp-container &> /dev/null

echo -e "${GREEN} בונה את ה-Image...${NC}"
docker build -t royapp .

if [ $? -ne 0 ]; then
    echo -e "${RED} הבנייה נכשלה.${NC}"
    exit 1
fi

echo -e "${GREEN}📦 מריץ את הקונטיינר...${NC}"
docker run -d -p 3000:3000 --name royapp-container royapp

if [ $? -ne 0 ]; then
    echo -e "${RED} לא הצלחנו להריץ את הקונטיינר.${NC}"
    exit 1
fi

sleep 2
echo -e "${GREEN} האפליקציה רצה! גש ל: http://localhost:3000${NC}"

# מחיקת הקונטיינר וה-Image (אופציונלי)
# echo -e "${GREEN}🧹 מנקה...${NC}"
# docker stop myapp-container &> /dev/null
# docker rm myapp-container &> /dev/null
# docker rmi myapp &> /dev/null
