// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_interfaces:action/RobotTask.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACES__ACTION__DETAIL__ROBOT_TASK__BUILDER_HPP_
#define ROBOT_INTERFACES__ACTION__DETAIL__ROBOT_TASK__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robot_interfaces/action/detail/robot_task__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robot_interfaces
{

namespace action
{

namespace builder
{

class Init_RobotTask_Goal_destination
{
public:
  Init_RobotTask_Goal_destination()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_interfaces::action::RobotTask_Goal destination(::robot_interfaces::action::RobotTask_Goal::_destination_type arg)
  {
    msg_.destination = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::action::RobotTask_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::action::RobotTask_Goal>()
{
  return robot_interfaces::action::builder::Init_RobotTask_Goal_destination();
}

}  // namespace robot_interfaces


namespace robot_interfaces
{

namespace action
{

namespace builder
{

class Init_RobotTask_Result_message
{
public:
  explicit Init_RobotTask_Result_message(::robot_interfaces::action::RobotTask_Result & msg)
  : msg_(msg)
  {}
  ::robot_interfaces::action::RobotTask_Result message(::robot_interfaces::action::RobotTask_Result::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::action::RobotTask_Result msg_;
};

class Init_RobotTask_Result_success
{
public:
  Init_RobotTask_Result_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotTask_Result_message success(::robot_interfaces::action::RobotTask_Result::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_RobotTask_Result_message(msg_);
  }

private:
  ::robot_interfaces::action::RobotTask_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::action::RobotTask_Result>()
{
  return robot_interfaces::action::builder::Init_RobotTask_Result_success();
}

}  // namespace robot_interfaces


namespace robot_interfaces
{

namespace action
{

namespace builder
{

class Init_RobotTask_Feedback_progress
{
public:
  Init_RobotTask_Feedback_progress()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_interfaces::action::RobotTask_Feedback progress(::robot_interfaces::action::RobotTask_Feedback::_progress_type arg)
  {
    msg_.progress = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::action::RobotTask_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::action::RobotTask_Feedback>()
{
  return robot_interfaces::action::builder::Init_RobotTask_Feedback_progress();
}

}  // namespace robot_interfaces


namespace robot_interfaces
{

namespace action
{

namespace builder
{

class Init_RobotTask_SendGoal_Request_goal
{
public:
  explicit Init_RobotTask_SendGoal_Request_goal(::robot_interfaces::action::RobotTask_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::robot_interfaces::action::RobotTask_SendGoal_Request goal(::robot_interfaces::action::RobotTask_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::action::RobotTask_SendGoal_Request msg_;
};

class Init_RobotTask_SendGoal_Request_goal_id
{
public:
  Init_RobotTask_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotTask_SendGoal_Request_goal goal_id(::robot_interfaces::action::RobotTask_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_RobotTask_SendGoal_Request_goal(msg_);
  }

private:
  ::robot_interfaces::action::RobotTask_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::action::RobotTask_SendGoal_Request>()
{
  return robot_interfaces::action::builder::Init_RobotTask_SendGoal_Request_goal_id();
}

}  // namespace robot_interfaces


namespace robot_interfaces
{

namespace action
{

namespace builder
{

class Init_RobotTask_SendGoal_Response_stamp
{
public:
  explicit Init_RobotTask_SendGoal_Response_stamp(::robot_interfaces::action::RobotTask_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::robot_interfaces::action::RobotTask_SendGoal_Response stamp(::robot_interfaces::action::RobotTask_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::action::RobotTask_SendGoal_Response msg_;
};

class Init_RobotTask_SendGoal_Response_accepted
{
public:
  Init_RobotTask_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotTask_SendGoal_Response_stamp accepted(::robot_interfaces::action::RobotTask_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_RobotTask_SendGoal_Response_stamp(msg_);
  }

private:
  ::robot_interfaces::action::RobotTask_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::action::RobotTask_SendGoal_Response>()
{
  return robot_interfaces::action::builder::Init_RobotTask_SendGoal_Response_accepted();
}

}  // namespace robot_interfaces


namespace robot_interfaces
{

namespace action
{

namespace builder
{

class Init_RobotTask_GetResult_Request_goal_id
{
public:
  Init_RobotTask_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_interfaces::action::RobotTask_GetResult_Request goal_id(::robot_interfaces::action::RobotTask_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::action::RobotTask_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::action::RobotTask_GetResult_Request>()
{
  return robot_interfaces::action::builder::Init_RobotTask_GetResult_Request_goal_id();
}

}  // namespace robot_interfaces


namespace robot_interfaces
{

namespace action
{

namespace builder
{

class Init_RobotTask_GetResult_Response_result
{
public:
  explicit Init_RobotTask_GetResult_Response_result(::robot_interfaces::action::RobotTask_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::robot_interfaces::action::RobotTask_GetResult_Response result(::robot_interfaces::action::RobotTask_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::action::RobotTask_GetResult_Response msg_;
};

class Init_RobotTask_GetResult_Response_status
{
public:
  Init_RobotTask_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotTask_GetResult_Response_result status(::robot_interfaces::action::RobotTask_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_RobotTask_GetResult_Response_result(msg_);
  }

private:
  ::robot_interfaces::action::RobotTask_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::action::RobotTask_GetResult_Response>()
{
  return robot_interfaces::action::builder::Init_RobotTask_GetResult_Response_status();
}

}  // namespace robot_interfaces


namespace robot_interfaces
{

namespace action
{

namespace builder
{

class Init_RobotTask_FeedbackMessage_feedback
{
public:
  explicit Init_RobotTask_FeedbackMessage_feedback(::robot_interfaces::action::RobotTask_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::robot_interfaces::action::RobotTask_FeedbackMessage feedback(::robot_interfaces::action::RobotTask_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::action::RobotTask_FeedbackMessage msg_;
};

class Init_RobotTask_FeedbackMessage_goal_id
{
public:
  Init_RobotTask_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotTask_FeedbackMessage_feedback goal_id(::robot_interfaces::action::RobotTask_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_RobotTask_FeedbackMessage_feedback(msg_);
  }

private:
  ::robot_interfaces::action::RobotTask_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::action::RobotTask_FeedbackMessage>()
{
  return robot_interfaces::action::builder::Init_RobotTask_FeedbackMessage_goal_id();
}

}  // namespace robot_interfaces

#endif  // ROBOT_INTERFACES__ACTION__DETAIL__ROBOT_TASK__BUILDER_HPP_
