a1={
    code:'COMP1601',
    type:'Assignment',
    start_date:'23/10/2023',
    start_time:'11:00 PM',
    end_date:'29/10/2023',
    end_time:'11:00PM'
}

a2={
    code:'COMP1601',
    type:'Assignment',
    start_date:'23/11/2023',
    start_time:'11:00 PM',
    end_date:'29/11/2023',
    end_time:'11:00PM'
}

a3={
    code:'COMP1603',
    type:'Assignment',
    start_date:'03/12/2023',
    start_time:'11:00 PM',
    end_date:'03/12/2023',
    end_time:'11:00PM'
}

a4={
    code:'COMP1603',
    type:'Exam',
    start_date:'23/01/2024',
    start_time:'11:00 PM',
    end_date:'23/01/2024',
    end_time:'11:00PM'
}


assessments=[a1,a2,a3,a4]
const cardContainer = document.getElementById('card_container');

assessments.forEach(assessment => {
    // Create the card element
    const card = document.createElement('div');
    card.classList.add('card');
    card.setAttribute('data-course-code', assessment.code);
    
    // Create elements for course details, assessment info, and actions
    const courseDetails = document.createElement('div');
    courseDetails.classList.add('course-details');
    const assessmentInfo = document.createElement('div');
    assessmentInfo.classList.add('assessment-info');
    const actions = document.createElement('div');
    actions.classList.add('actions');

    // Create content for course details
    const courseCodeLabel = document.createElement('p');
    courseCodeLabel.classList.add('card-label');
    courseCodeLabel.textContent = 'Course Code';
    const courseCode = document.createElement('p');
    courseCode.classList.add('course-code');
    courseCode.textContent = assessment.code;

    const courseAssessmentLabel = document.createElement('p');
    courseAssessmentLabel.classList.add('card-label');
    courseAssessmentLabel.textContent = 'Assessment Type';
    const assessmentType = document.createElement('p');
    assessmentType.classList.add('assessment-type');
    assessmentType.textContent = assessment.type;

    const startDateLabel = document.createElement('p');
    startDateLabel.classList.add('card-label');
    startDateLabel.textContent = 'Start Date';
    const startDate = document.createElement('p');
    startDate.classList.add('start-date');
    startDate.textContent = assessment.start_date+" - "+assessment.start_time;

    const endDateLabel = document.createElement('p');
    endDateLabel.classList.add('card-label');
    endDateLabel.textContent = 'End Date';
    const endDate = document.createElement('p');
    endDate.classList.add('end-date');
    endDate.textContent = assessment.end_date+" - "+assessment.end_time;

    // Create action links (modify and delete can be replaced with actual functionality)
    const modifyLink = document.createElement('button');
    modifyLink.textContent = 'Modify';
    modifyLink.addEventListener('click', function() {
        window.location.href = `/modifyAssessment/${assessment.code}`;
    });
    const deleteLink = document.createElement('button');
    deleteLink.textContent = 'Delete';
    deleteLink.classList.add('delete_btn')
    deleteLink.href = '#'; // Replace with actual delete functionality

    // Append elements to their respective parents
    courseDetails.appendChild(courseCodeLabel);
    courseDetails.appendChild(courseCode);
    assessmentInfo.appendChild(courseAssessmentLabel);
    assessmentInfo.appendChild(assessmentType);
    courseDetails.appendChild(startDateLabel);
    courseDetails.appendChild(startDate);
    assessmentInfo.appendChild(endDateLabel);
    assessmentInfo.appendChild(endDate);
    actions.appendChild(modifyLink);
    actions.appendChild(deleteLink);
    card.appendChild(courseDetails);
    card.appendChild(assessmentInfo);
    card.appendChild(actions);

    // Append the card to the card container
    cardContainer.appendChild(card);
});